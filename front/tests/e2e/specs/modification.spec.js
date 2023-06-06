describe('modification', () => {
    it('Test', () => {
        const mail = 'tim@mail.com'
        const password = 'tim'
        cy.visit('/login');
        cy.get('input[id=login-email]').type(mail);
        cy.get('input[id=login-pw]').type(password);
        cy.get('button[type=submit]').click();
        cy.url().should('equal', `${Cypress.config('baseUrl')}/`);

        cy.wait(500);

        cy.get('#all-hotels button').first().click()

        cy.get('input[id=nom]').clear().type('Belambra');
        cy.get('textarea[id=description]').clear().type('Un hotel à Marseille');
        cy.get('input[id=prix]').clear().type(85);
        cy.get('button.my-button.hover-button').eq(1).click();
        cy.get('button.my-button.hover-button').first().click();
        cy.url().should('equal', `${Cypress.config('baseUrl')}/`);

        cy.wait(500);

        cy.get('#all-hotels button').first().click()
        cy.get('input[id=nom]').invoke('val').should('equal', 'Belambra');
        cy.get('textarea[id=description]').invoke('val').should('equal', 'Un hotel à Marseille');
        cy.get('input[id=prix]').invoke('val').should('equal', '85');

        cy.get('input[id=prix]').clear().type(-45);
        cy.get('button.my-button.hover-button').eq(1).click();
        cy.get('div.my-alert').should('be.visible');
        cy.get('button.my-button.hover-button').first().click();
        cy.url().should('equal', `${Cypress.config('baseUrl')}/`);

        cy.wait(500);

        cy.get('#all-hotels button').first().click()
        cy.get('div.my-alert').should('not.exist');
        cy.get('input[id=prix]').invoke('val').should('equal', '85');

    })
})