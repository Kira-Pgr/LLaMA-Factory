from llmtuner import create_ui


def main():
    demo = create_ui()
    demo.queue()
    demo.launch(share=True, inbrowser=False)


if __name__ == "__main__":
    main()
