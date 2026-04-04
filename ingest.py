import io
import zipfile
import requests
import frontmatter
import yaml

from minsearch import Index


def read_repo_data(repo_owner, repo_name):
    url = f"https://github.com/{repo_owner}/{repo_name}/archive/refs/heads/main.zip"
    resp = requests.get(url)

    repository_data = []

    zf = zipfile.ZipFile(io.BytesIO(resp.content))

    for file_info in zf.infolist():
        filename = file_info.filename.lower()

        if not (filename.endswith('.md') or filename.endswith('.mdx')):
            continue

        with zf.open(file_info) as f_in:
            # We decode to string here to ensure frontmatter parses it correctly
            # (Sometimes reading directly from zip returns bytes which can cause issues)
            try:
                content = f_in.read().decode('utf-8') 
            except UnicodeDecodeError:
                print(f"⚠️ Skipping {file_info.filename}: Not a valid UTF-8 text file.")
                continue

            try:
                # Attempt to parse the YAML frontmatter
                post = frontmatter.loads(content)
                data = post.to_dict()

                _, filename_repo = file_info.filename.split('/', maxsplit=1)
                data['filename'] = filename_repo
                repository_data.append(data)
                
            except yaml.YAMLError as e:
                # Skip files with broken YAML headers
                print(f"⚠️ Skipping {file_info.filename} due to broken frontmatter: {e}")
                continue
            except Exception as e:
                # Catch any other unexpected parsing errors
                print(f"⚠️ Error reading {file_info.filename}: {e}")
                continue

    zf.close()

    return repository_data


def sliding_window(seq, size, step):
    if size <= 0 or step <= 0:
        raise ValueError("size and step must be positive")

    n = len(seq)
    result = []
    for i in range(0, n, step):
        batch = seq[i:i+size]
        result.append({'start': i, 'content': batch})
        if i + size > n:
            break

    return result


def chunk_documents(docs, size=2000, step=1000):
    chunks = []

    for doc in docs:
        doc_copy = doc.copy()
        doc_content = doc_copy.pop('content')
        doc_chunks = sliding_window(doc_content, size=size, step=step)
        for chunk in doc_chunks:
            chunk.update(doc_copy)
        chunks.extend(doc_chunks)

    return chunks


def index_data(
        repo_owner,
        repo_name,
        filter=None,
        chunk=True,
        chunking_params={'size': 1000, 'step': 500}
    ):
    docs = read_repo_data(repo_owner, repo_name)

    if filter is not None:
        docs = [doc for doc in docs if filter(doc)]

    if chunk:
        if chunking_params is None:
            chunking_params = {'size': 2000, 'step': 1000}
        docs = chunk_documents(docs, **chunking_params)

    index = Index(
        text_fields=["content", "filename"],
    )

    index.fit(docs)
    return index
