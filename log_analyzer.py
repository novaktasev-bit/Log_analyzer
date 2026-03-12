def check_error (error):
    if "error" in error.lower():
        return 1
    else:
        return 0

total_messages = 0
error_count = 0
error_list = []

while True:
    user_input = input("Enter you message or type 'stop': ")
    if user_input.lower() == 'stop':
        break
    else:
        error_count += check_error(user_input)
        total_messages +=1

        if check_error(user_input) == 1:
            error_list.append(user_input)
          
print("\n===ERROR ANALYZE===")
print(f"Total messages: {total_messages}")
print(f"Error count: {error_count}")

if total_messages > 0:
    error_rate = (error_count / total_messages) * 100
    print(f"Error rate is: {error_rate:.2f}%")
else:
    print("No message to analyze.")

if error_list:
    print("\n===DETAILED ERROR LIST===")
    for single_error in error_list:
        print(single_error)
else: 
    print("There is not an error list.")
