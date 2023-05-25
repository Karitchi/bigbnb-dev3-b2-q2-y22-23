import { shallowMount } from '@vue/test-utils';
import BackButton from '@/components/Hotel/BackButton.vue';
import { useRouter } from 'vue-router';

describe('BackButton', () => {
    it('calls router.back when Go Back button is clicked', () => {
        // Mock the useRouter function
        jest.spyOn(require('vue-router'), 'useRouter').mockReturnValue({
            back: jest.fn(),
        });

        // Render the component
        const wrapper = shallowMount(BackButton);

        // Find the Go Back button and trigger a click event
        const goBackButton = wrapper.find('.btn-primary');
        goBackButton.trigger('click');

        // Assert that router.back has been called
        expect(require('vue-router').useRouter().back).toHaveBeenCalled();
    });

    it('renders the Go Back button with the correct class', () => {
        // Render the component
        const wrapper = shallowMount(BackButton);

        // Find the Go Back button
        const goBackButton = wrapper.find('.btn-primary');

        // Assert that the button exists and has the expected class
        expect(goBackButton.exists()).toBe(true);
        expect(goBackButton.classes()).toContain('btn-primary');
    });

    it('calls router.back when goBack function is called', () => {
        // Mock the useRouter function
        jest.spyOn(require('vue-router'), 'useRouter').mockReturnValue({
            back: jest.fn(),
        });

        // Render the component
        const wrapper = shallowMount(BackButton);

        // Call the goBack function
        wrapper.vm.goBack();

        // Assert that router.back has been called
        expect(require('vue-router').useRouter().back).toHaveBeenCalled();
    });
});
