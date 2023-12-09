# flyup
A tool to find minimal spell fly up speed modification stacks for Noita, it has terrible time complexity, but is garunteed to find optimal solutions.
It automatically divides by 7.92 to account for 0.99 dampening 8 velocity tentacle, though you can easily remove this.
Error is a relative ratio of the target, so 0.01 error is ~= +- 1% error.
For extremely hard to find searches it might be worth toggling some of the log comments on any solution found on, or enabling the change to make it decrease error bars after finding a solution if you aren't sure how precise you can get.
Final output is sorted by 4 * unique spells + total spells, best solutions at bottom. Fly up is not taken into account.
