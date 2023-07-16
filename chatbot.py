import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Cargar el libro en formato de texto
book_text = """
Aquí iría el texto completo del libro que deseas analizar.
"""

# Tokenización de palabras y oraciones
sentences = sent_tokenize(book_text)
word_tokens = word_tokenize(book_text)

# Eliminación de palabras vacías y lematización
stop_words = set(stopwords.words('spanish'))
lemmatizer = WordNetLemmatizer()

filtered_tokens = [lemmatizer.lemmatize(token.lower()) for token in word_tokens if token.lower() not in stop_words]

# Construcción de índice de búsqueda
index = {}
for i, sentence in enumerate(sentences):
    words = word_tokenize(sentence)
    filtered_words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in stop_words]
    for word in filtered_words:
        if word not in index:
            index[word] = []
        index[word].append(i)

# Función de búsqueda
def search(query):
    query_tokens = word_tokenize(query)
    query_words = [lemmatizer.lemmatize(word.lower()) for word in query_tokens if word.lower() not in stop_words]
    
    results = set()
    for word in query_words:
        if word in index:
            results.update(index[word])
    
    return [sentences[i] for i in results]

# Ejemplo de búsqueda
query = "buscar esto en el libro"
search_results = search(query)
for result in search_results:
    print(result)

