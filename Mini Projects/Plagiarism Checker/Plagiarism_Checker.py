import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_plagiarism():
    # 1. Get all .txt files in the current directory
    files = [f for f in os.listdir() if f.endswith('.txt')]
    
    if len(files) < 2:
        print("❌ Error: You need at least two .txt files in the folder to compare.")
        return

    # 2. Read the content of each file
    notes = [open(f, encoding='utf-8').read() for f in files]

    # 3. Convert text to Vectors (numbers that represent word importance)
    # Tfidf stands for Term Frequency-Inverse Document Frequency
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(notes)

    # 4. Compare each file with every other file
    print(f"--- Plagiarism Report ({len(files)} files scanned) ---\n")
    
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            # Calculate similarity score (0 to 1)
            score = cosine_similarity(vectors[i], vectors[j])[0][0]
            
            # Convert to percentage
            percentage = score * 100
            
            print(f"Comparing '{files[i]}' and '{files[j]}':")
            print(f"Similarity Score: {percentage:.2f}%\n")

if __name__ == "__main__":
    check_plagiarism()