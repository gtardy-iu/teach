run_cnt = 0

with open('steps.txt', 'r') as f:
    while (line := f.readline().strip()) != '':
        if int(line) > 5000:
            run_cnt += 1
        print(line)

print(run_cnt)

with open('report.txt', 'w') as f:
    f.write(f'Day count for over 5000 steps, {run_cnt}')
    f.write('\n')
