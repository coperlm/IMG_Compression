# remove_brackets_regex.py
import argparse
import io
import re
from pathlib import Path

def remove_brackets_regex(text: str) -> str:
    # 非贪婪模式 + DOTALL 使点号匹配换行
    return re.sub(r'\[.*?\]', '', text, flags=re.S)

def main():
    p = argparse.ArgumentParser(description="删除文件中所有方括号 [...] 及其内部内容（简单正则版，不能正确处理嵌套）。")
    p.add_argument("input", help="输入文件路径")
    p.add_argument("-o", "--output", help="输出文件路径（不指定则覆盖输入文件）")
    args = p.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path

    text = input_path.read_text(encoding="utf-8")
    new_text = remove_brackets_regex(text)
    output_path.write_text(new_text, encoding="utf-8")
    print(f"已写入 {output_path}")

if __name__ == "__main__":
    main()
