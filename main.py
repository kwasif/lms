# Main script for a Library Management System

from models import Models


def main():
    # Load library information
    lms_model_obj = Models()
    # Launch the application
    lms_model_obj.start()


if __name__ == "__main__":
    main()
