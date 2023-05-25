import {toRef} from "vue";


describe('Test My-Hotels', () => {
    it('Test', () => {
        // cy.visit('/my_hotels');

        const mail = 'tim@mail.com'
        const password = 'tim'
        cy.visit('/login');
        cy.get('input[id=login-email]').type(mail);
        cy.get('input[id=login-pw]').type(password);
        cy.get('button[type=submit]').click();
        cy.url().should('equal', `${Cypress.config('baseUrl')}/`);

        cy.wait(500);

        const hotel = 'Ibis';
        cy.visit('/my_hotels');
        cy.get('[href="/my_hotels"]').should('have.class', 'disabled');
        cy.get('[href="/my_bookings"').should('have.class', 'active');
        cy.get('input[id=my-hotels-search]').type(hotel);
        cy.get('#all-hotels button').first().click();
        cy.url().should('include', '/modification');
        cy.visit('/my_hotels');

        cy.get('[href="/my_bookings"]').click();
        cy.get('[href="/my_hotels"]').should('have.class', 'active');
        cy.get('[href="/my_bookings"').should('have.class', 'disabled');
        testButtonApprove('btn-success');
        testButtonApprove('btn-danger');
        cy.get('body').then($body => {
           while ($body.find('.btn-success').length > 0) {
               testButtonApprove('btn-success');
           }
        });
        cy.get('.btn-success').should('not.exist').then(() => {
            cy.get('#all-bookings').should('contain.text', "Pas de bookings");
        });

        cy.get('[data-test-id="button-disconnect"]').click();
        cy.url().should('equal', `${Cypress.config('baseUrl')}/`);

    })
});

describe('Test filter', () => {
    it('testNormal', () => {
        let min_price = 0
        let max_price = 200
        let min_room = 0
        let max_room = 90

        cy.visit('http://127.0.0.1:8080/filter_hotels')
        cy.get('input[id=min_price]').focus().clear().type(min_price).should('have.attr', 'type', 'number');
        cy.get('input[id=max_price]').focus().clear().type(max_price).should('have.attr', 'type', 'number');
        cy.get('input[id=min_room]').focus().clear().type(min_room).should('have.attr', 'type', 'number');
        cy.get('input[id=max_room]').focus().clear().type(max_room).should('have.attr', 'type', 'number');

        cy.wait(500);

        cy.get('div.hotels-list ul li').should('have.length', 1);

        cy.get('button.btn').click()
        cy.get('h3.cart-title').should('contain.text', "Test");

        min_price = 0
        max_price = 200
        min_room = 0
        max_room = 500
        cy.visit('http://127.0.0.1:8080/filter_hotels')
        cy.get('input[id=min_price]').focus().clear().type(min_price).should('have.attr', 'type', 'number');
        cy.get('input[id=max_price]').focus().clear().type(max_price).should('have.attr', 'type', 'number');
        cy.get('input[id=min_room]').focus().clear().type(min_room).should('have.attr', 'type', 'number');
        cy.get('input[id=max_room]').focus().clear().type(max_room).should('have.attr', 'type', 'number');
        
        cy.get('div.hotels-list ul li').should('have.length', 4);

        cy.contains('button.btn.btn-outline-primary', "Plus d'informations").should(($elements) => {
                expect($elements.eq(0)).to.have.text("Plus d'informations");
                // expect($elements.eq(1)).to.have.text("Plus d'informations");
                // expect($elements.eq(2)).to.have.text("Plus d'informations");
                // expect($elements.eq(3)).to.have.text("Plus d'informations");
        });

    })
});


function testButtonApprove(buttonType) {
    cy.get('body').then($body => {
        if ($body.find(`.${buttonType}`).length > 0) {
            cy.get(`.${buttonType}`).then($elements => {
                const length = $elements.length;
                cy.get(`.${buttonType}`).first().click();
                cy.get(`.${buttonType}`).should($updateElements => {
                    expect($updateElements.length).to.eq(length - 1);
                });
            });
        }
    });
}
