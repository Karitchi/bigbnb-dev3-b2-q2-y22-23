import { mount } from '@vue/test-utils';
import Modification from '@/views/modification.vue';

describe('Modification', () => {
  test('goBack method navigates back', () => {
    const wrapper = mount(Modification);
    const goBackButton = wrapper.find('button.my-button');
    goBackButton.trigger('click');
    expect(wrapper.vm.$route.path).toBe('/');
  });

  test('modifierHotel method updates hotel data', () => {
    const wrapper = mount(Modification);
    wrapper.setData({
      name: 'Test Hotel',
      description: 'Test Description',
      price: 100,
    });
    wrapper.vm.modifierHotel();

    // Ajoutez des assertions pour vérifier que les données de l'hôtel sont mises à jour correctement
    expect(wrapper.vm.hotel.name).toBe('Test Hotel');
    expect(wrapper.vm.hotel.description).toBe('Test Description');
    expect(wrapper.vm.hotel.price).toBe(100);
  });

  test('displays error message for invalid hotel name', () => {
    const wrapper = mount(Modification);
    wrapper.setData({ name: 'A' });
    wrapper.vm.modifierHotel();
    expect(wrapper.vm.errorForm).toBe("Le nom de l'hôtel doit contenir entre 3 et 30 caractères.");
  });

  test('displays error message for invalid hotel price', () => {
    const wrapper = mount(Modification);
    wrapper.setData({ price: -100 });
    wrapper.vm.modifierHotel();
    expect(wrapper.vm.errorForm).toBe('Le prix de la chambre doit être supérieur à zéro');
  });

  // Ajoutez d'autres tests ici pour les autres méthodes et les validations de formulaire

});