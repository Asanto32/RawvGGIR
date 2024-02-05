**GGIR implementation guide:**



**Phase 1: Calibration, calculate ENMO and anglez**

- [Calibration:](#calibration)
  - [Summary of process:](#summary-of-process)
- [Calcuate metrics](#calcuate-metrics)


# Calibration:
We expect that for non-movement time the applied g-force acting on the sensor should be 1g. Find non-movement time, compare data points during this time to unit sphere. Solve a fitting problem (apply scale and offset to data) to get those points as close as possible to unit sphere. Then apply this scale and offset to all data:

$$
\tilde{s_i}(t) = a_i * s_i(t) + b_i
$$

Where, $s_i$ is the initial accelerometer data for each i-th dimension, $a_i$ is the scaling factor, $b_i$  is the offset factor, and $\tilde{s_i}$ is the calibrated accelerometer signal.

## Summary of process:
1. Find non-movement times: 
   - Defined as when SD(acc[x,y,z])<0.013 over 10s window
   - This is done by downsampling acc[x,y,z]. 
   - Then SD over each window. 
   - Identify windows where SD, in all 3 axes, is < cutoff_value (default 0.013). Keep only those windows. Also, “& npall( abs(roll_mean(acc))<2)”, to ‘avoid clipping’ (removes with large mean no SD).

2. Check for sufficient data points + "sphere well populated"

# Calcuate metrics