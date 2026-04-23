from src.cli import build_parser, render_output


def main() -> None:

    args = build_parser().parse_args()
    output = render_output(args.domain, args.json)
    print(output)
    if args.file:
        ext = "json" if args.json else "txt"
        with open(f"{args.domain}_result.{ext}", "w", encoding="utf-8") as file:
            file.write(output)


if __name__ == "__main__":
    main()
