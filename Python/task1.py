import re


# Задание 1

# Функция без регулярных выражений.
# Работает в рекурсивном режиме:
# вызывает себя при открытии скобки в тексте и ищет закрывающую скобку для себя

def text_editor(text, is_open=False):
    answer = ""
    index_start = 0  # вспомогаетльный индекс
    index = 0  # индекс текущего элемента в тексте
    while index < len(text):
        if text[index] == "(":
            answer += text[index_start:index]
            a, b = text_editor(text[index + 1:], is_open=True)
            answer += a
            index += b
            index_start = index
            continue

        elif text[index] == ")" and is_open:
            return "", index + 2

        index += 1

    if is_open:
        answer = "(" + answer
    answer += text[index_start:index]

    if is_open:
        return answer, index + 1

    return answer


def text_editor_re(text):
    n = 1  # run at least once
    while n:
        text, n = re.subn(r'\([^()]*\)', '', text)
    return text


def main():
    text = "asdflj (kla (inner) asd) port (another ))(unclosed"
    print(f"Без регулярных выражений:\n{text_editor(text)}")
    print(f"\nС регулярными выражениями:\n{text_editor_re(text)}")


if __name__ == "__main__":
    main()
