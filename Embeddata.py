import google.generativeai as genai
from chromadb import Documents, EmbeddingFunction, Embeddings
import os
from dotenv import load_dotenv

class GeminiEmbeddingFunction(EmbeddingFunction):
    """
    Custom embedding function using the Gemini AI API for document retrieval.

    This class extends the EmbeddingFunction class and implements the __call__ method
    to generate embeddings for a given set of documents using the Gemini AI API.

    Parameters:
    - input (Documents): A collection of documents to be embedded.

    Returns:
    - Embeddings: Embeddings generated for the input documents.
    """
    def __call__(self, input: Documents) -> Embeddings:
        # Load environment variables
        load_dotenv()
        gemini_api_key = os.getenv("GOOGLE_API_KEY")
        
        # Debug: print API key (remove this in production)
        
        if not gemini_api_key:
            raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as an environment variable")
        
        # Configure the generative AI API
        genai.configure(api_key=gemini_api_key)
        model = "models/embedding-001"
        title = "Custom query"
        
        # Generate embeddings
        response = genai.embed_content(model=model,
                                       content=input,
                                       task_type="retrieval_document",
                                       title=title)
        
        # Return the embeddings
        return response["embedding"]

# # Create an instance of the custom embedding function
# gemiNew = GeminiEmbeddingFunction()

# # Call the function with an example document
# embeddings = gemiNew(["This is a test document."])

# # Print the embeddings result
# print( len(embeddings))