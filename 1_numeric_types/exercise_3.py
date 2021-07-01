def run_timing():
    run_times = []
    while True:
        time = input("Enter 10 km run time (in minutes): ")

        if (time == ""):
            break

        run_times.append(float(time))

    print(f"Average of {sum(run_times) / len(run_times)} over {len(run_times)} runs")

run_timing()