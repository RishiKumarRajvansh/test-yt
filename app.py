from flask import Flask, request, jsonify, send_file
import yt_dlp
import os

app = Flask(__name__)

# Folder to save downloaded videos
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "Please provide a valid YouTube URL"}), 400

    try:
        # Set download options
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)  # Download video
            filename = ydl.prepare_filename(info)  # Get filename

        return send_file(filename, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
