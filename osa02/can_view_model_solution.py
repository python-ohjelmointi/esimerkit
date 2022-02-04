# Nämä tulevat "tietokannasta"
role = 'assistant'
has_solved = False

# Tästä eteenpäin koodi toimii annetuilla arvoilla
is_admin = (role == 'admin')
is_teacher = (role == 'teacher')
is_assistant = (role == 'assistant')
is_student = (role == 'student')
is_staff = is_admin or is_teacher or is_assistant

if is_staff or (is_student and has_solved):
    print('Saat nähdä malliratkaisun')

elif role != '':
    print("It seems like you haven't solved the exercise yet")

else:
    print('You need to log in')
