const addSkillButton = document.querySelector('#addSkill');
const skillsContainer = document.querySelector('#skillsContainer');

const skill = document.querySelector('#skill');

const addCourseButton = document.querySelector('#addCourse');
const coursesContainer  = document.querySelector('#coursesContainer');
const course = document.querySelector('#course');


const addLanguageButton = document.querySelector('#addLanguage');
const languagesContainer  = document.querySelector('#languagesContainer');
const language = document.querySelector('#language');

const languageLvl = document.querySelector('#languageLvl');

const submitButton = document.querySelector('#submitBtn');

loadEventListeners();


function loadEventListeners(){
    addSkillButton.addEventListener('click', addSkill);
    skillsContainer.addEventListener('click', removeSkill);

    addCourseButton.addEventListener('click', addCourse);
    coursesContainer.addEventListener('click', removeCourse);

    addLanguageButton.addEventListener('click', addLanguage);
    languagesContainer.addEventListener('click', removeLanguage);

    submitButton.addEventListener('click', submitCheck);
}


function submitCheck(e)
{
    if(skillsContainer.innerText==="")
    {
       const p = document.createElement('p');
       p.innerText = "Uzupełnij informacje o ofercie";
       p.id = "error";
       p.style = 'color:red;';
       skillsErrorMessages.appendChild(p);
       setTimeout(function(){
           document.querySelector('#error').remove();
       }, 3000);
    }else
    {
        document.getElementById("job_offer_form").submit();
    }
    e.preventDefault();
}


function addSkill(e){
    
    const skill_type = skill.value;
    
    const skillDiv = document.createElement('div');
    skillDiv.className='skillListElement';
    skillDiv.innerHTML = skill_type+" ";

    const hiddenChoice = document.createElement('input');
    hiddenChoice.name = 'skill';
    hiddenChoice.value = skill_type;
    hiddenChoice.style = 'display:none;';
    
    const p = document.createElement('p');
    
    
    const skillText = document.createElement('textarea');
    skillText.name = 'skillText';
    skillText.required = true;
    
    const delButton = document.createElement('a');
    delButton.className = 'delete-item';
    delButton.innerHTML = 'x';
    delButton.style = 'color:red;';

    const dateFromTitle = document.createElement('p');
    dateFromTitle.innerText = 'Data od';

    const dateFrom = document.createElement('input');
    dateFrom.type = 'date';
    dateFrom.name = "date_from";

    const dateToTitle = document.createElement('p');
    dateToTitle.innerText = 'Data do';

    const dateTo = document.createElement('input');
    dateTo.type = 'date';
    dateTo.name = "date_to";

    const presentTitle = document.createElement('p');
    presentTitle.innerText = "Obecnie";
    
    const presentSelect = document.createElement('select');
    presentSelect.name = 'present';
    presentSelect.innerHTML = '<option value="False">Nie</option><option value="True">Tak</option>';

    skillDiv.appendChild(delButton);
    skillDiv.appendChild(p);
    skillDiv.appendChild(hiddenChoice);
    skillDiv.appendChild(skillText);
    skillDiv.appendChild(dateFromTitle);
    skillDiv.appendChild(dateFrom);
    skillDiv.appendChild(dateToTitle);
    skillDiv.appendChild(dateTo);
    skillDiv.appendChild(presentTitle);
    skillDiv.appendChild(presentSelect);
    


    skillsContainer.appendChild(skillDiv);
    
    e.preventDefault();
}

function removeSkill(e){
    if(e.target.classList.contains('delete-item'))
    {
        e.target.parentElement.remove();
    }
}



function addLanguage(e){
    language.removeAttribute("name");
    languageLvl.removeAttribute("name");

    const language_type = language.value;
    const languageLvl_type = languageLvl.value;
    
    const languageDiv = document.createElement('div');
    languageDiv.className = 'languageListElement';

    const hiddenLanguage = document.createElement('input');
    hiddenLanguage.name = 'language';
    hiddenLanguage.value  = language_type;
    hiddenLanguage.style = 'display:none;';

    const hiddenLanguageLvl = document.createElement('input');
    hiddenLanguageLvl.name = 'languageLvl';
    hiddenLanguageLvl.value  = languageLvl_type;
    hiddenLanguageLvl.style = 'display:none;';

    languageDiv.innerHTML = language_type+": "+languageLvl_type+" ";
    
    const delButton = document.createElement('a');
    delButton.className = 'delete-item';
    delButton.innerHTML = 'x';
    delButton.style = 'color:red;';
    languageDiv.appendChild(hiddenLanguage);
    languageDiv.appendChild(hiddenLanguageLvl);
    
    languageDiv.appendChild(delButton);

    languagesContainer.appendChild(languageDiv);

    e.preventDefault();

}

function removeLanguage(e){
    if(e.target.classList.contains('delete-item'))
    {
        e.target.parentElement.remove();
    }
    if(languagesContainer.innerText ==="")
    {
        language.setAttribute("name", "language");
        languageLvl.setAttribute("name", "languageLvl");
    }
}

function addCourse(e){
    course.removeAttribute("name");

    const course_type = course.value;
    
    const courseDiv = document.createElement('div');
    courseDiv.className = 'courseListElement';

    const hiddenCourse = document.createElement('input');
    hiddenCourse.name = 'course';
    hiddenCourse.value  = course_type;
    hiddenCourse.style = 'display:none;';

    courseDiv.innerHTML = course_type+" ";
    
    const delButton = document.createElement('a');
    delButton.className = 'delete-item';
    delButton.innerHTML = 'x';
    delButton.style = 'color:red;';

    courseDiv.appendChild(hiddenCourse);
    courseDiv.appendChild(delButton);

    coursesContainer.appendChild(courseDiv);

    e.preventDefault();

}

function removeCourse(e){
    if(e.target.classList.contains('delete-item'))
    {
        e.target.parentElement.remove();
    }
    if(coursesContainer.innerText ==="")
    {
        course.setAttribute("name", "course");
    }
}