class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pref = [0 for _ in range(101)] 
        
        for birth, death in logs:
            pref[birth - 1950] += 1
            pref[death - 1950] -= 1
        
        for idx in range(1, len(pref)):
            pref[idx] += pref[idx - 1]

        max_population = 0
        result = -1
        for idx, population in enumerate(pref):
            if population > max_population:
                max_population = population
                result = idx
        return result + 1950
        
