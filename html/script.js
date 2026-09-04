// Função principal que calcula o IMC
function calcularIMC() {

    // Captura o valor do peso digitado
    const peso = parseFloat(document.getElementById("peso").value);

    // Captura o valor da altura digitada
    const altura = parseFloat(document.getElementById("altura").value);

    // Verifica se os valores são válidos
    if (!peso || !altura || altura <= 0) {
        // Exibe mensagem de erro
        document.getElementById("resultado").innerText = "Por favor, insira valores válidos.";
        return; // Sai da função se os dados forem inválidos
    }

    // Calcula o IMC e arredonda para 2 casas decimais
    const imc = (peso / (altura * altura)).toFixed(2);

    // Cria variável para guardar a classificação
    let classificacao = "";

    // Estrutura condicional para definir a classificação
    if (imc < 18.5) {
        classificacao = "Abaixo do peso";
    } else if (imc < 24.9) {
        classificacao = "Peso normal";
    } else if (imc < 29.9) {
        classificacao = "Sobrepeso";
    } else {
        classificacao = "Obesidade";
    }

    // Exibe resultado final na tela
    document.getElementById("resultado").innerText = `Seu IMC é ${imc} (${classificacao}).`;
}
