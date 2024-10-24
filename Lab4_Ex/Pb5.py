def read_bmp_file(filename):
    with open(filename, 'rb') as f:
        header = f.read(14)
        file_type = header[0:2].decode('ascii')
        file_size = int.from_bytes(header[2:6], 'little')
        pixel_offset = int.from_bytes(header[10:14], 'little')

        dib_header = f.read(40)
        width = int.from_bytes(dib_header[4:8], 'little')
        height = int.from_bytes(dib_header[8:12], 'little')
        bits_per_pixel = int.from_bytes(dib_header[14:16], 'little')

        print(f"File type: {file_type}")
        print(f"File size: {file_size} bytes")
        print(f"Image offset: {pixel_offset} bytes")
        print(f"Image width: {width} pixels")
        print(f"Image height: {height} pixels")
        print(f"Bits per pixel: {bits_per_pixel}")

        f.seek(pixel_offset)

        row_size = ((bits_per_pixel * width + 31) // 32) * 4  
        pixel_data = []
        for y in range(height):
            row = f.read(row_size) 
            pixels = []
            for x in range(width):
                if bits_per_pixel == 24:
                    blue = row[x*3]
                    green = row[x*3+1]
                    red = row[x*3+2]
                    pixels.append(f"({red},{green},{blue})")
            pixel_data.append(pixels)

        for row in pixel_data[::-1]:
            print(' '.join(row))


read_bmp_file('python.bmp')
