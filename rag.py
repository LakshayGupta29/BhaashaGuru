"""
RAG (Retrieval-Augmented Generation) System for BhaashaGuru
Handles document retrieval from NCERT PDFs
"""
import os
import json
from pathlib import Path
from typing import List, Tuple
import config


class SimpleRAGSystem:
    """
    A simple CPU-based RAG system using sentence-transformers and FAISS.
    Loads documents from text files and provides retrieval functionality.
    """
    
    def __init__(self, docs_path: str = config.NCERT_DOCS_PATH):
        """
        Initialize the RAG system.
        
        Args:
            docs_path: Path to directory containing NCERT documents
        """
        self.docs_path = docs_path
        self.documents = []
        self.embedder = None
        self.index = None
        self.chunk_size = config.CHUNK_SIZE
        self.chunk_overlap = config.CHUNK_OVERLAP
        self.top_k = config.TOP_K_CHUNKS
        self._initialized = False
        
        if os.path.exists(docs_path):
            self._load_documents()
    
    def _load_documents(self):
        """Load documents from the docs directory."""
        try:
            import faiss
            from sentence_transformers import SentenceTransformer
            
            # Initialize embedder
            self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
            
            # Load all text files
            for file in Path(self.docs_path).glob("*.txt"):
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    chunks = self._chunk_text(content, file.stem)
                    self.documents.extend(chunks)
            
            if self.documents:
                self._build_index()
                self._initialized = True
                print(f"[RAG] Loaded {len(self.documents)} document chunks")
            else:
                print("[RAG] No documents found in docs path")
        
        except ImportError as e:
            print(f"[RAG] Warning: Required libraries not available: {e}")
            self._initialized = False
    
    def _chunk_text(self, text: str, source: str) -> List[dict]:
        """
        Split text into overlapping chunks.
        
        Args:
            text: The text to chunk
            source: Source document name
        
        Returns:
            List of chunk dictionaries
        """
        chunks = []
        words = text.split()
        
        # Simple word-based chunking
        for i in range(0, len(words), self.chunk_size - self.chunk_overlap):
            chunk_words = words[i:i + self.chunk_size]
            if chunk_words:
                chunks.append({
                    "text": " ".join(chunk_words),
                    "source": source,
                    "index": i
                })
        
        return chunks
    
    def _build_index(self):
        """Build FAISS index from document embeddings."""
        try:
            import faiss
            import numpy as np
            
            # Embed all documents
            embeddings = self.embedder.encode(
                [doc["text"] for doc in self.documents],
                convert_to_tensor=False
            )
            
            # Create FAISS index
            dimension = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dimension)
            self.index.add(embeddings.astype('float32'))
            
            print(f"[RAG] Built FAISS index with dimension {dimension}")
        
        except Exception as e:
            print(f"[RAG] Error building index: {e}")
            self.index = None
    
    def retrieve(self, query: str, top_k: int = None) -> List[str]:
        """
        Retrieve relevant documents for a query.
        
        Args:
            query: The search query
            top_k: Number of results to return (uses config value if None)
        
        Returns:
            List of relevant document chunks
        """
        if not self._initialized or self.index is None:
            return []
        
        top_k = top_k or self.top_k
        
        try:
            # Embed query
            query_embedding = self.embedder.encode([query], convert_to_tensor=False)
            
            # Search
            distances, indices = self.index.search(query_embedding.astype('float32'), top_k)
            
            # Retrieve results
            results = []
            for idx in indices[0]:
                if 0 <= idx < len(self.documents):
                    results.append(self.documents[idx]["text"])
            
            return results
        
        except Exception as e:
            print(f"[RAG] Error during retrieval: {e}")
            return []
    
    def get_context_string(self, query: str, top_k: int = None) -> str:
        """
        Get retrieved context as a formatted string.
        
        Args:
            query: The search query
            top_k: Number of results
        
        Returns:
            Formatted context string
        """
        results = self.retrieve(query, top_k)
        if not results:
            return ""
        
        context = "Relevant NCERT Content:\n"
        for i, result in enumerate(results, 1):
            context += f"\n{i}. {result[:200]}..."  # Truncate for brevity
        
        return context


# Global RAG instance
_rag_instance = None


def get_rag_system() -> SimpleRAGSystem:
    """Get or create the global RAG system instance."""
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = SimpleRAGSystem()
    return _rag_instance


def retrieve_context(query: str) -> str:
    """
    Retrieve and format context for a query.
    
    Args:
        query: The search query
    
    Returns:
        Formatted context string
    """
    if not config.USE_RAG:
        return ""
    
    rag = get_rag_system()
    return rag.get_context_string(query)
