import yt_dlp
import os


def download_playlist(playlist_url, output_dir):
    ydl_opts = {
        "format": "bestaudio",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "FFmpegMetadata"},
            {"key": "EmbedThumbnail"},
        ],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "writethumbnail": True,
        "ignoreerrors": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    playlist_url = input("Enter the playlist URL: ")
    output_dir = "./output"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    download_playlist(playlist_url, output_dir)
    print("\n" + "=" * 30 + "\nDownload completed!\n" + "=" * 30)
    print("Downloaded files are saved in:", os.path.abspath(output_dir))
