/**
 * Profile functions
 */

function profile() {

    function submitAddressAction(button){
        const form = document.getElementById('form-template');
        let input = document.createElement("input");
        let id = 'sgadddqwbnwdddwdgqg2bwbdbdd';
        form.method = 'post';
        form.action = button.dataset.url;
        input.name = "address_id";
        input.id = 'sgadddqwbnwdddwdgqg2bwbdbdd';
        input.type = "hidden";
        input.value = button.dataset.id;

        let inp = document.getElementById(id);
        if (inp){
            inp.parentElement.removeChild(inp);
        }
        form.appendChild(input);

        if (button.id === 'delete_address'){
            console.log(button.dataset.id, button.name, button.id);
            if (! confirm("Do you really want to delete this address?")){
                return;
            }
        }
        form.submit();
    }

    // Listeners
    document.addEventListener('DOMContentLoaded', (e) => {
        const actionButtons = document.getElementsByClassName('address-action');
        for (let bt of actionButtons){
            bt.addEventListener('click', (e)=>{
                submitAddressAction(e.currentTarget)
            })
        }
    });
} // EOF profile

profile();