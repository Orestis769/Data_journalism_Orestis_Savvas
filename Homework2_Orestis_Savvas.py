#1) Ας υποθέσουμε ότι είμαστε πολύ κακοί γιατροί και έχουμε έναν ασθενή.
#Ορίστε ένα λεξικό που να λέγεται patient και θα δουλεύει με τον παρακάτω κώδικα.

patient = {
'name': 'Orestis Savvas',
'complaint':'πυρετό', 
}
print(f"Γιατρέ, ο ασθενής {patient["name"]} παραπονιέται ότι έχει", patient['complaint'])

#2) Δεν δίνουμε πολύ σημασία στον ασθενή, αλλά όσο έρχονται νέα αποτελέσματα εξετάσεων, τα προσθέτουμε στο λεξικό του ασθενή:
patient.update({'Heart rate': 70, 'Temperature': 98.6, 'Infection': 'No'}) 
#Τυπώστε τα keys του λεξικού
print(patient.keys())
print(patient)

##3) Τώρα ας γίνουμε γιατροί! Πρώτα πρέπει αν έχουν heart rate ίσο ή μεγαλύτερο από το 100, πρέπει να τους πούμε να ηρεμήσουν.
if patient['Heart rate'] >= 100:
    print("Παρακαλώ ηρεμήστε, ο καρδιακός σας ρυθμός είναι υψηλός.")
    #Αποθηκεύστε τη διάγνωση σας σε ένα κλειδί (key) που θα λέγεται 'diagnosis'.
    patient['diagnosis'] = 'High heart rate'
else:
    print("Ο καρδιακός σας ρυθμός είναι φυσιολογικός.")
    
#Αν έχουν temperature πάνω από 102, αλλά δεν έχουν infection, έχουν πάθει θερμοπληξία.

#Αν έχουν temperature πάνω από 102 και έχουν και infection, τότε έχουν γρίπη.

#Αν έχουν infection αλλά όχι temperature πάνω από 102 τότε είναι έχουν ένα απλό κρύωμα.

#Αν δεν έχουν τίποτα από τα παραπάνω πείτε τους να πάρουν μία ασπιρίνη και να σας τηλεφωνήσουν το πρωί.

if patient['Temperature'] > 102 and patient['Infection'] == 'No':
    print("Έχετε πάθει θερμοπληξία.")
    patient['diagnosis'] = 'Heat stroke'
elif patient['Temperature'] > 102 and patient['Infection'] == 'Yes':
    print("Έχετε γρίπη.")
    patient['diagnosis'] = 'Flu'
elif patient['Infection'] == 'Yes' and patient['Temperature'] <= 102:
    print("Έχετε ένα απλό κρύωμα.")
    patient['diagnosis'] = 'Cold'
else:
    print("Παρακαλώ πάρτε μία ασπιρίνη και τηλεφωνήστε μου το πρωί.")
    patient['diagnosis'] = 'No serious illness'
    
#Όταν τελειώσετε με την παραπάνω λούπα, τυπώστε: "Το όνομα του ασθενή από το λεξικό, η διάγνωσή σου είναι _______."
print(f"Το όνομα του ασθενή είναι {patient['name']}, η διάγνωσή σου είναι {patient['diagnosis']}.") 
#5 Δεύτερο Λεξικό Βρείτε ποιοι από τους επόμενους ασθενείς έχουν πάθει θερμοπληξία.
#patients_2 = [ {'name': 'Beast', 'Temperature': 99}, {'name': 'Simba', 'Temperature': 105}, {'name': 'Snowwhite', 'Temperature': 98}, {'name': 'Donald', 'Temperature': 99}, {'name': 'Bambi', 'Temperature': 100}, {'name': 'Aladdin', 'Temperature': 104}, {'name': 'Hercules', 'Temperature': 105}, {'name': 'Frollo', 'Temperature': 100}]
patients_2 = [ {'name': 'Beast', 'Temperature': 99}, {'name': 'Simba', 'Temperature': 105}, {'name': 'Snowwhite', 'Temperature': 98}, {'name': 'Donald', 'Temperature': 99}, {'name': 'Bambi', 'Temperature': 100}, {'name': 'Aladdin', 'Temperature': 104}, {'name': 'Hercules', 'Temperature': 105}, {'name': 'Frollo', 'Temperature': 100}]
for patient in patients_2:
    if patient['Temperature'] > 102:
        print(f"{patient['name']} έχει πάθει θερμοπληξία.") 

#6 Σώστε τις διαγνώσεις σε μια λίστα που θα λέγεται records
records = []
for patient in patients_2:  
    if patient['Temperature'] > 102:
        records.append({'name': patient['name'], 'diagnosis': 'Heat stroke'})
    else:
        records.append({'name': patient['name'], 'diagnosis': 'No serious illness'})
print(records)