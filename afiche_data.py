import pysrt

def display_first_subtitles(file_path):
    try:
        subs = pysrt.open(file_path, encoding='utf-8')
        print(f"The first 5 subtitles from the file '{file_path}':\n")
        for i, sub in enumerate(subs[:5], start=1):
            print(f"Subtitle {i}:")
            print(f"Time: {sub.start} --> {sub.end}")
            print(f"Text: {sub.text}\n")
    except FileNotFoundError:
        print(f"The file '{file_path}' could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file_path = "file\to\data.srt"
    display_first_subtitles(file_path)
