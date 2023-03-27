const ResponseMixin = {
    methods: {
        handleSuccess(form, alertSuccess, alertError,data) {
            form.reset();
            form.classList.remove('was-validated');
            alertError.classList.add('d-none');
            const alertMessage = alertSuccess.querySelector('#alert_message_id');
            alertMessage.innerHTML = data.message;
            alertSuccess.classList.remove('d-none');
        },
  
        handleError(alertSuccess, alertDanger, data) {
            // alert(data.message);
            alertSuccess.classList.add("d-none");
            const alertMessage = alertDanger.querySelector('#alert_message_id');
            alertMessage.innerHTML = data.message;
            alertDanger.classList.remove("d-none");
        },
    },
};

const FormSubmitMixin = {
    mixins: [ResponseMixin],
    methods: {
        async submitForm(event) {
            event.preventDefault();
            const form = event.target;
            const url = form.action;
            const method = form.method
            const csrfToken = form.getAttribute("data-csrf");
            const alertSuccess = form.querySelector('#alert_success_id');
            const alertDanger = form.querySelector('#alert_danger_id');
            const formData = new FormData(form);
            const response = await fetch(url, {
                method: method,
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken,
                },
            });
            if (response.ok) {
                const data = await response.json();
                if (data.status == 201){
                    ResponseMixin.methods.handleSuccess(form, alertSuccess, alertDanger, data);
                    // console.log(data.status);
                    // form.reset();
                    // form.classList.remove("was-validated");
                    // alertDanger.classList.add("d-none");
                    // const alertMessage = alertSuccess.querySelector('.alert-message');
                    // alertMessage.innerHTML = data.message;
                    // alertSuccess.classList.remove("d-none");
                    // alert(data.message);
                }else{
                    ResponseMixin.methods.handleError(alertSuccess, alertDanger, data);
                    // alert(data.message);
                    // alertSuccess.classList.add("d-none");
                    // const alertMessage = alertDanger.querySelector('#alert_message_id');
                    // alertMessage.innerHTML = data.message;
                    // alertDanger.innerHTML = data.message;
                    // alertDanger.classList.remove("d-none");
                }
            } else {
                alert(data.message);
                const alertMessage = alertDanger.querySelector('#alert_message_id');
                alertMessage.innerHTML = data.message;
                alertDanger.classList.remove("d-none");
            }
        },
    },
};

// const form_cliente = document.getElementById("create_cliente_form_id");
// Object.assign(form_cliente, FormSubmitMixin.methods);
// form_cliente.addEventListener("submit", form_cliente.submitForm);

// const form_venda = document.getElementById("create_venda_form_id");
// Object.assign(form_venda, FormSubmitMixin.methods);
// form_venda.addEventListener("submit", form_venda.submitForm);

// const form_analise = document.getElementById("create_analise_form_id");
// Object.assign(form_analise, FormSubmitMixin.methods);
// form_analise.addEventListener("submit", form_analise.submitForm);


const closeButtons = document.querySelectorAll('.btn-close');
    closeButtons.forEach(function(closeButton) {
      closeButton.addEventListener('click', function() {
        const alert = this.parentNode;
        alert.classList.toggle('d-none');
    });
});