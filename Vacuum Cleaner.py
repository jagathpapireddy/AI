def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

def run_simulation():
  
    location = "A"
    room_states = {"A": "Dirty", "B": "Dirty"}
    total_cost = 0 
    
    print(f"Initial Location: {location}, States: {room_states}\n")
    
    for step in range(3):
        status = room_states[location]
        action = reflex_agent(location, status)

        total_cost += 1 
        
        print(f"Step {step + 1}: At {location}, Status: {status} -> Action: {action} (Cumulative Cost: {total_cost})")
        
        if action == "Suck":
            room_states[location] = "Clean"
        elif action == "Right":
            location = "B"
        elif action == "Left":
            location = "A"
            
    print(f"\nFinal States: {room_states}")
    print(f"Total Operational Cost: {total_cost}")

if __name__ == "__main__":
    run_simulation()
