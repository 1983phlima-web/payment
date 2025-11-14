## APPSTRIPE
Autor: Paulo Lima
Data: 13/11/2025
Versão: 1.0


# POC Marketplace com Stripe Connect
Este é um exemplo bem simples de uma aplicação web em Flask demonstrando como usar o Stripe Connect para criar um marketplace. 
A aplicação permite que um cliente compre um produto de um vendedor, e a plataforma automaticamente cobra uma taxa de aplicação.


# Como executar
1.  Instale as dependências:

    pip install Flask stripe


2.  Exponha as suas chaves de API do Stripe:

    export STRIPE_SECRET_KEY=sk_test_... 
    export STRIPE_PUBLIC_KEY=pk_test_...
 

3.  Execute a aplicação:

    python AppStripe.py


4.  Acesse a aplicação em seu navegador:

    [http://localhost:5000](http://localhost:5000)


# Fluxo
1.  O cliente clica no botão "Pagar".
2.  A aplicação cria uma sessão de checkout no Stripe.
3.  O cliente é redirecionado para a página de pagamento do Stripe.
4.  Após o pagamento, o Stripe redireciona o cliente para a página de sucesso.
5.  O valor do pagamento é transferido para a conta conectada do vendedor, e a plataforma recebe a taxa de aplicação.
