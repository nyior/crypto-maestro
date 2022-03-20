import asyncio

from app.cli import main_cli


if __name__ == "__main__":
    import platform

    if platform.system() == "Windows": # Had issues with getting it to work on Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main_cli())
