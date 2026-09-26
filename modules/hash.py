import hashlib

#text = "Hello World!"
#hash_object = hashlib.sha256(text.encode())
#hash_digest = hash_object.hexdigest()
#print("The SHA256 hash is: ", text, "is", hash_digest)

def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path, "rb") as file:
        while True: 
            chunk = file.read(1024)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    print ("\nChecking integrity between ", file1, " and ", file2)
    if hash1 == hash2:
        return "File is intact. No Modification has been made."
    return "File has been modified. It is unsafe"

if __name__ == "__main__":
    import os
    base_dir = os.path.join(os.path.dirname(__file__), "..", "sample_files")
    print("The SHA of File is: ", hash_file(os.path.join(base_dir, "sample.txt")))
    print(verify_integrity(os.path.join(base_dir, "1788520701783_3802183315728945632_3802183315728945632_87d690015549eaf221a30fb434af09bc 1.jpg"), os.path.join(base_dir, "1788520701783_3802183315728945632_3802183315728945632_87d690015549eaf221a30fb434af09bc 2.jpg")))
    print(verify_integrity(os.path.join(base_dir, "1788520701783_3802183315728945632_3802183315728945632_87d690015549eaf221a30fb434af09bc 2.jpg"), os.path.join(base_dir, "1788520701783_3802183315728945632_3802183315728945632_87d690015549eaf221a30fb434af09bc 3.jpg")))
    print(verify_integrity(os.path.join(base_dir, "1788520701783_3802183315728945632_3802183315728945632_87d690015549eaf221a30fb434af09bc 3.jpg"), os.path.join(base_dir, "1788520701783_3802183315728945632_3802183315728945632_87d690015549eaf221a30fb434af09bc 4.jpg")))