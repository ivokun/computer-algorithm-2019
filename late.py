MAX_LATE = 3
LATE_PROB = 0.5
DAYS = 20

def compute_late(days = DAYS, maxLate = MAX_LATE, lateProb = LATE_PROB, saved = None):
  if saved == None: saved = {}
  ID = (days, maxLate, lateProb)
  if ID in saved: return saved[ID]
  else:
    if maxLate > days or days <= 0:
      result = 0
    else:
      result = lateProb ** maxLate
      for late in range(1, maxLate+1):
        prob = compute_late(days-maxLate, maxLate, lateProb, saved)
        result += (lateProb**(late-1))*(1-lateProb)*prob
    saved[ID] = result
    return result

print(compute_late())
  