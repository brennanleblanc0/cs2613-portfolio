function is_factorial(x) {
    if (x < 0) {
        return -1;
    } else if (x == 0) {
        return 0;
    }

    let doneFact = false;
    let divisor = 1;

    while (!doneFact) {
        if (x % divisor == 0 && x / divisor != 1) {
            x /= divisor;
            divisor++;
        } else if (x % divisor == 0 && x / divisor == 1) {
            doneFact = true;
            return divisor;
        } else {
            doneFact = true;
            return 0;
        }
    }
}
