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


loadEventListeners();

function loadEventListeners(){
    addSkillButton.addEventListener('click', addSkill);
    skillsContainer.addEventListener('click', removeSkill);

    addCourseButton.addEventListener('click', addCourse);
    coursesContainer.addEventListener('click', removeCourse);

    addLanguageButton.addEventListener('click', addLanguage);
    languagesContainer.addEventListener('click', removeLanguage);
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

    skillDiv.appendChild(delButton);
    skillDiv.appendChild(p);
    skillDiv.appendChild(hiddenChoice);
    skillDiv.appendChild(skillText);
    
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
    const language_type = language.value;
    const languageLvl_type = languageLvl.value;
    
    const languageDiv = document.createElement('div');
    languageDiv.className = 'languageListElement';

    const hiddenLanguage = document.createElement('input');
    hiddenLanguage.name = 'language';
    hiddenLanguage.value  = language_type;
    hiddenLanguage.style = 'display:none;';

    const hiddenLanguageLvl = document.createElement('input');
    hiddenLanguageLvl.name = 'language';
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
}

function addCourse(e){
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
}