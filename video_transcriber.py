import whisper
import os

def video_to_text(video_path):
    try:
        # Load whisper model (will download on first run)
        print("Loading speech recognition model...")
        model = whisper.load_model("base")
        
        print("Transcribing video...")
        # Transcribe the audio
        result = model.transcribe(video_path)
        
        # Save transcription to text file
        output_path = os.path.splitext(video_path)[0] + "_transcript.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
            
        print(f"Transcription saved to: {output_path}")
        return True
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    video_file = input("Enter video filename: ")
    video_to_text(video_file)