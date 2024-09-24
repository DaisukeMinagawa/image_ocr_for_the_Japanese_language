import sys
import pytesseract
from PIL import Image


def extract_text(image_path):
    # 画像を開く
    image = Image.open(image_path)

    # Tesseractを使用して日本語テキストを抽出
    text = pytesseract.image_to_string(image, lang='jpn')

    return text


def save_text(text, output_file):
    # テキストをファイルに保存
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)


def main():
    if len(sys.argv) != 2:
        print("使用方法: python tesseract.py <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]
    image_path = input("画像ファイルのパスを入力してください: ")

    # テキストを抽出
    extracted_text = extract_text(image_path)

    # テキストを保存
    save_text(extracted_text, output_file)

    print(f"テキストが {output_file} に保存されました。")


if __name__ == "__main__":
    main()