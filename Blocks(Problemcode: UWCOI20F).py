def prime_factor(n):
   prime_list = []
   count_list = []
   prime = 2
   while prime ** 2 < n + 1:
      if n % prime == 0:
         n = n // prime
         if prime in prime_list:
            count_list[-1] += 1
         else:
            prime_list.append(prime)
            count_list.append(1)
      else:
         prime += 1
   if n in prime_list:
      count_list[-1] += 1
   else:
      prime_list.append(n)
      count_list.append(1)
   return [prime_list, count_list]

tests = int(input())
for _ in range(tests):
   n, q = [int(j) for j in input().split()]
   primes, counts = prime_factor(n)
   answered = False
   answer = 1
   while q > 0:
      if sum(counts) == 0:
         answered = True
         print("! "+str(n//answer))
         break
      if counts[0] == 0:
         counts.pop(0)
         primes.pop(0)
      prime_power = (counts[0]+1) // 2
      question = answer
      for prime, count in zip(primes,counts):
         question *= prime ** count
      question = question // (primes[0] ** prime_power)
      print("? "+str(question))
      reply = int(input())
      if reply + question != n:
         answer *= primes[0] ** prime_power
      counts[0] -= prime_power
      q -= 1
   if not answered:
      print("! "+str(n//answer))
   valid = int(input())
