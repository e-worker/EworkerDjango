const addSkillButton = document.querySelector('#addSkill');
const skillsContainer = document.querySelector('#skillsContainer');
const skill = document.querySelector('#skill');

loadEventListeners();

function loadEventListeners(){
    addSkillButton.addEventListener('click', addSkill);
    skillsContainer.addEventListener('click', removeSkill);
}

function addSkill(e){
    const skill_type = skill.value;
    const skillDiv = document.createElement('div');
    skillDiv.className='skillListElement';
    const hiddenChoice = document.createElement('input');
    hiddenChoice.name = 'skill';
    hiddenChoice.value = skill_type;
    hiddenChoice.style = 'display:none;';
    const title = document.createElement('p');
    title.innerHTML = skill_type;
    const skillText = document.createElement('textarea');
    skillText.name = 'skillText';
    const delButton = document.createElement('a');
    delButton.className = 'delete-item';
    delButton.innerHTML = 'x';
    skillDiv.appendChild(title);
    skillDiv.appendChild(delButton);
    skillDiv.appendChild(hiddenChoice);
    skillDiv.appendChild(skillText);
    skillsContainer.appendChild(skillDiv);
    e.preventDefault();
}

function removeSkill(e){
    console.log(e.target);
    if(e.target.classList.contains('delete-item'))
    {
        e.target.parentElement.remove();
    }
}