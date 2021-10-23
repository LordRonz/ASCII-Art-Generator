from ASCII_art_gen import generate_art
from parser import get_args

def main():
    args = get_args()
    input_filename = args['source_file'].name
    args['source_file'].close()
    output_filename = args['output'] or 'out.png'
    generate_art(input_filename, output_filename, args['color'])

if __name__ == '__main__':
    main()
