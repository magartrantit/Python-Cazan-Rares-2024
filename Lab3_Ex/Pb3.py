def print_table(text):
    text_to_bytes = text.encode('utf-8')

    header = "     " + " ".join([f"{i:02X}" for i in range(16)])
    spacer = "    +" + "-" * (len(header) - 1)

    print(header)
    print(spacer)

    for i in range(0, len(text_to_bytes), 16):
        left = f"{i:04X}"

        partition = text_to_bytes[i:i + 16]
        right = " ".join(f"{byte:02X}" for byte in partition)
        print(f"{left} | {right}")



input_text = "Acesta este un exemplu."
print_table(input_text)