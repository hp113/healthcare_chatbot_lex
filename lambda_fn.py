import json
import boto3

client = boto3.client('dynamodb')

def validate_ah(slots):
    # Parameter validation
    if not slots['Height']:
        return {'isValid': False, 'violatedSlot': 'Height'}
    elif int(slots['Height']['value']['originalValue']) <= 100:
        return {'isValid': False, 'violatedSlot': 'Height'}
    if not slots['Weight']:
        return {'isValid': False, 'violatedSlot': 'Weight'}
    elif int(slots['Weight']['value']['originalValue']) <= 20:
        return {'isValid': False, 'violatedSlot': 'Weight'}
    if not slots['HeartRate']:
        return {'isValid': False, 'violatedSlot': 'HeartRate'}
    elif int(slots['HeartRate']['value']['originalValue']) <= 40:
        return {'isValid': False, 'violatedSlot': 'HeartRate'}
    if not slots['SystolicBP']:
        return {'isValid': False, 'violatedSlot': 'SystolicBP'}
    elif int(slots['SystolicBP']['value']['originalValue']) <= 20:
        return {'isValid': False, 'violatedSlot': 'SystolicBP'}
    if not slots['DiastolicBP']:
        return {'isValid': False, 'violatedSlot': 'DiastolicBP'}
    elif int(slots['DiastolicBP']['value']['originalValue']) <= 20:
        return {'isValid': False, 'violatedSlot': 'DiastolicBP'}
    if not slots['Sugar']:
        return {'isValid': False, 'violatedSlot': 'Sugar'}
    elif int(slots['Sugar']['value']['originalValue']) <= 0:
        return {'isValid': False, 'violatedSlot': 'Sugar'}
    if not slots['Cholesterol']:
        return {'isValid': False, 'violatedSlot': 'Cholesterol'}
    elif int(slots['Cholesterol']['value']['originalValue']) <= 0:
        return {'isValid': False, 'violatedSlot': 'Cholesterol'}
    if not slots['StepsWalked']:
        return {'isValid': False, 'violatedSlot': 'StepsWalked'}
    elif int(slots['StepsWalked']['value']['originalValue']) <= 0:
        return {'isValid': False, 'violatedSlot': 'StepsWalked'}
    if not slots['SleepQuality']:
        return {'isValid': False, 'violatedSlot': 'SleepQuality'}
    elif int(slots['SleepQuality']['value']['originalValue']) <= 0:
        return {'isValid': False, 'violatedSlot': 'SleepQuality'}
    if not slots['SleepHours']:
        return {'isValid': False, 'violatedSlot': 'SleepHours'}
    elif int(slots['SleepHours']['value']['originalValue']) <= 0:
        return {'isValid': False, 'violatedSlot': 'SleepHours'}

    return {'isValid': True}

def validate_sa(slots):
    if not slots['Name']:
        print("Name not present")
        return {
            'isValid': False,
            'violatedSlot': 'Name'
        }
    if not slots['Height']:
        return {'isValid': False, 'violatedSlot': 'Height'}
    elif int(slots['Height']['value']['originalValue']) <= 100:
        return {'isValid': False, 'violatedSlot': 'Height'}
    if not slots['Weight']:
        return {'isValid': False, 'violatedSlot': 'Weight'}
    elif int(slots['Weight']['value']['originalValue']) <= 20:
        return {'isValid': False, 'violatedSlot': 'Weight'}
    
    return {'isValid': True}

def validate_sm(slots):
    if not slots['PersonName']:
        print("Person Name not present")
        return {
            'isValid': False,
            'violatedSlot': 'PersonName'
        }        
        
    if not slots['Symptoms']:
        return {
            'isValid': False,
            'violatedSlot': 'Symptoms',
        }
    if not slots['symptomDuration']:
        return {
            'isValid': False,
            'violatedSlot': 'symptomDuration',
        }
    if not slots['symptomSeverity']:
        return {
            'isValid': False,
            'violatedSlot': 'symptomSeverity',
        }
    elif not (1 <= int(slots['symptomSeverity']['value']['originalValue']) <= 10):
        return {'isValid': False, 'violatedSlot': 'symptomSeverity'}

    return {'isValid': True}

def validate_ba(slots):
    if not slots['Name']:
        print("Name not present")
        return {
            'isValid': False,
            'violatedSlot': 'Name'
        }
    if not slots['Age']:
        return {'isValid': False, 'violatedSlot': 'Age'}
    elif int(slots['Age']['value']['originalValue']) <= 17:
        return {'isValid': False, 'violatedSlot': 'Age'}
    
    if not slots['Location']:
        return{
            'isValid':False,
            'violatedSlot':'Location'
        }
    if not slots['Date']:
        return{
            'isValid':False,
            'violatedSlot':'Date'
        }
    if not slots['Time']:
        return{
            'isValid':False,
            'violatedSlot':'Time'
        }
    
    return {'isValid': True}

def assess_health(slots):
    height = int(slots['Height']['value']['originalValue']);
    weight = int(slots['Weight']['value']['originalValue']);
    resting_heart_rate = int(slots['HeartRate']['value']['originalValue']);
    systolic = int(slots['SystolicBP']['value']['originalValue']);
    diastolic = int(slots['DiastolicBP']['value']['originalValue']);
    blood_sugar = int(slots['Sugar']['value']['originalValue']);
    cholesterol = int(slots['Cholesterol']['value']['originalValue']);
    physical_activity = int(slots['StepsWalked']['value']['originalValue']);
    sleep_quality = int(slots['SleepQuality']['value']['originalValue']);
    sleep_duration = int(slots['SleepHours']['value']['originalValue']);

    health_status = ""
    #Calculate BMI using Height Weight
    height_in_m = height/100
    bmi = weight/(height_in_m**2 )
    # Assess BMI
    health_status +="BMI Status: "
    if bmi < 18.5:
        health_status += "Underweight\n"
    elif bmi >= 18.5 and bmi < 25:
        health_status += "Normal weight\n"
    elif bmi >= 25 and bmi < 30:
        health_status += "Overweight\n"
    else:
        health_status += "Obese\n"

    # Assess Resting Heart Rate
    health_status +="| Heart Rate: "
    if resting_heart_rate < 60:
        health_status += "Low\n"
    elif resting_heart_rate >= 60 and resting_heart_rate <= 100:
        health_status += "Normal\n"
    else:
        health_status += "High\n"

    # Assess Blood Pressure
    if systolic < 120 and diastolic < 80:
        health_status += "| Blood Pressure: Normal\n"
    elif systolic >= 120 and systolic < 130 and diastolic < 80:
        health_status += "| Blood Pressure: Elevated\n"
    
    elif systolic >= 130 and systolic < 140 or diastolic >= 80 and diastolic < 90:
        health_status += "| Hypertension: Stage 1\n"
    else:
        health_status += "| Hypertension: Stage 2\n"

    # Assess Blood Sugar Levels
    health_status +="| Blood Sugar level: "
    if blood_sugar < 100:
        health_status += "Normal\n"
    elif blood_sugar >= 100 and blood_sugar < 126:
        health_status += "Prediabetes\n"
    else:
        health_status += "Diabetes\n"

    # Assess Cholesterol Levels
    health_status +="| Cholesterol: "
    if cholesterol < 200:
        health_status += "Desirable\n"
    elif cholesterol >= 200 and cholesterol < 240:
        health_status += "Borderline\n"
    else:
        health_status += "High\n"

    # Assess Physical Activity Levels
    health_status +="| Physical Activity: "
    if physical_activity < 5000:
        health_status += "Low\n"
    elif physical_activity >= 5000 and physical_activity < 10000:
        health_status += "Moderate\n"
    else:
        health_status += "High\n"

    # Assess Sleep Quality and Duration
    health_status +="| Sleep Quality & Duration: "
    if sleep_quality >= 7 and sleep_duration >= 7:
        health_status += "Good\n"
    else:
        health_status += "Poor\n"

    return health_status

def bmi_advice(slots):
    height = int(slots['Height']['value']['originalValue'])
    weight = int(slots['Weight']['value']['originalValue'])
    height_in_m = height/100
    bmi = weight/(height_in_m**2 )
    print("bmi is" + str(bmi))
    if bmi < 18.5:
        return ("It looks like you may be malnourished. It's important to consult with a healthcare professional for personalized advice. "
                "In the meantime, focusing on nutrient-dense foods like fruits, vegetables, whole grains, and lean proteins can help improve your nutrition. "
                "Focus on strength-building exercises to help build muscle mass. Include exercises like weight lifting, bodyweight exercises (e.g., push-ups, squats), "
                "and resistance band exercises. Aim for at least 3 days of strength training per week, with a day of rest in between each session. Additionally, "
                "include aerobic exercises like walking, jogging, or cycling to improve overall fitness.")
    elif bmi > 18.5 and bmi < 24.9:
        return ("You're in the normal BMI range, which is great! To maintain your weight and overall health, focus on a balanced diet with plenty of fruits, "
                "vegetables, whole grains, and lean proteins. Regular exercise, such as cardio and strength training, can also help you stay healthy. "
                "Maintain your weight by engaging in regular physical activity. Aim for at least 150 minutes of moderate-intensity aerobic activity per week, "
                "such as brisk walking, swimming, or cycling. Include strength training exercises at least 2 days per week, targeting major muscle groups. "
                "Consider incorporating flexibility and balance exercises, such as yoga or tai chi, to improve overall fitness.")
    elif bmi > 25 and bmi < 29.9:
        return ("You are in the overweight category, which can increase the risk of health problems. To manage your weight, focus on a healthy diet low in processed "
                "foods and high in fruits, vegetables, whole grains, and lean proteins. Regular exercise, such as cardio and strength training, can also be beneficial. "
                "Focus on aerobic exercises to help burn calories and improve cardiovascular health. Aim for at least 150 minutes of moderate-intensity aerobic activity "
                "per week. Include strength training exercises to build muscle mass and improve metabolism. Aim for at least 2 days of strength training per week, "
                "targeting major muscle groups. Consider incorporating high-intensity interval training (HIIT) to increase calorie burn and improve fitness.")
    elif bmi > 30:
        return ("You are in the morbidly obese category, which poses serious health risks. It's crucial to seek professional help to manage your weight and improve "
                "your health. A healthcare provider can offer personalized advice on diet and exercise. Consider incorporating more fruits, vegetables, whole grains, "
                "and lean proteins into your diet. Regular physical activity, such as walking, swimming, or cycling, can also be beneficial. Consult with a healthcare "
                "professional or a certified trainer before starting any exercise program. Start with low-impact exercises like water aerobics, gentle yoga, or chair "
                "exercises to avoid putting too much strain on joints. Gradually increase the intensity and duration of your workouts as you become more comfortable and fit.")
    
def prescribe_medicine(symptoms, severity):
    severity = int(severity)  # Convert severity to integer
    if symptoms.lower() == 'cold':
        if severity >= 7:
            return "For a severe cold, it's advisable to consult a doctor. In the meantime, you may take over-the-counter cold medicine like acetaminophen or ibuprofen."
        elif severity >= 4:
            return "For a moderate cold, you may take over-the-counter cold medicine like acetaminophen or ibuprofen and ensure you get plenty of rest and fluids."
        else:
            return "For a mild cold, consider taking over-the-counter cold medicine like acetaminophen or ibuprofen and getting adequate rest."
    elif symptoms.lower() == 'cough':
        if severity >= 7:
            return "For a severe cough, it's best to consult a doctor. In the meantime, you may try cough syrup or lozenges to soothe your throat."
        elif severity >= 4:
            return "For a moderate cough, you may try cough syrup or lozenges to soothe your throat and ensure you get plenty of rest and fluids."
        else:
            return "For a mild cough, consider trying cough syrup or lozenges to soothe your throat and getting adequate rest."
    elif symptoms.lower() == 'headache':
        if severity >= 7:
            return "For a severe headache, it's advisable to consult a doctor. In the meantime, you may take pain relievers such as ibuprofen or acetaminophen."
        elif severity >= 4:
            return "For a moderate headache, you may take pain relievers such as ibuprofen or acetaminophen and ensure you rest in a quiet, dark room."
        else:
            return "For a mild headache, consider taking pain relievers such as ibuprofen or acetaminophen and practicing relaxation techniques."
    elif symptoms.lower() == 'fever':
        if severity >= 7:
            return "For a high fever, it's important to consult a doctor immediately. In the meantime, you can take over-the-counter fever reducers such as acetaminophen or ibuprofen and ensure you stay hydrated."
        elif severity >= 4:
            return "For a moderate fever, you may take over-the-counter fever reducers such as acetaminophen or ibuprofen, rest, and drink plenty of fluids."
        else:
            return "For a mild fever, consider taking over-the-counter fever reducers such as acetaminophen or ibuprofen, staying hydrated, and resting."
    else:
        return "It's recommended to consult a doctor for personalized advice based on your symptoms and severity."



def bookAppointment(slots):
    data = client.put_item(
        TableName='HealthCareChatBotDB',
        Item={
            'Name':{
                'S':slots['Name']['value']['originalValue']
            },
            'Age':{
                'S':slots['Age']['value']['originalValue']
            },
            'Location':{
                'S':slots['Location']['value']['originalValue']
            },
            'Date':{
                'S':slots['Date']['value']['originalValue']
            },
            'Time':{
                'S':slots['Time']['value']['originalValue']
            },
        }
    )
    return "Your Appointment has been confirmed!"



def lambda_handler(event, context):
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    print(slots)
    if(intent=="AssessHealth"):
        validation_result = validate_ah(slots)
    
    elif(intent=="suggestActivites"):
        validation_result = validate_sa(slots)
    
    elif(intent=="suggestMedication"):
        validation_result = validate_sm(slots)
    
    elif(intent=="appointmentBook"):
        validation_result = validate_ba(slots)
    
    else:
        validation_result = None
    print(validation_result)
    if event['invocationSource'] == 'DialogCodeHook':
        if not validation_result['isValid']:
            response = {
                        "sessionState": {
                            "dialogAction": {
                                'slotToElicit':validation_result['violatedSlot'],
                                "type": "ElicitSlot"
                            },
                            "intent": {
                                'name':intent,
                                'slots': slots
                                
                                }
                        }
                       } 
        else:
            response = {
                            "sessionState": {
                                "dialogAction": {
                                    "type": "Delegate"
                                },
                                "intent": {
                                    'name':intent,
                                    'slots': slots
                                    
                                    }
                            }
                           }
                           
    if event['invocationSource'] == 'FulfillmentCodeHook':
        if(intent=="AssessHealth"):
            result = assess_health(slots)
    
        elif(intent=="suggestActivites"):
            result = bmi_advice(slots)
        
        elif(intent=="suggestMedication"):
            result = prescribe_medicine(slots['Symptoms']['value']['originalValue'], slots['symptomSeverity']['value']['originalValue'])
        
        elif(intent=="appointmentBook"):
            result = bookAppointment(slots)
        
        else:
            result = "Failed"
        
        response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                'name':intent,
                'slots': slots,
                'state':'Fulfilled'
                
                }
    
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": result
            }
        ]
    }                       
                           
    return response
