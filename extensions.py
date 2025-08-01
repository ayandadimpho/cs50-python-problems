file_name = input("What is the name of the file? ")
file_name = file_name.strip().lower()

if file_name.endswith((".jpeg",".png", ".jpg", "gif")):
    print("image")
elif file_name.endswith("pdf"):
    print("pdf")
elif file_name.endswith(".txt"):
    print("text")
elif file_name.endswith(".zip"):
    print("zip")
else:
    print("application/octet-stream")

