from util import calculate_happiness, setup_logger

def main():
    logger = setup_logger()
    logger.info("Reading input...")
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    logger.info("Calculating happiness...")
    happiness = calculate_happiness(n, m, arr, a, b)

    logger.info("Total happiness: %d", happiness)

if __name__ == "__main__":
    main()
