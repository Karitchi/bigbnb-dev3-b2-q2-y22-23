import { mount } from '@vue/test-utils'
import { defineProps } from 'vue'
import Carousel from '@/components/Hotel/CarousselGallery/Caroussel.vue'

describe('Carousel', () => {
    it('renders the carousel with the correct number of images and indicators', () => {
        const props = {
            urls: ['image1.jpg', 'image2.jpg', 'image3.jpg']
        }

        const wrapper = mount(Carousel, {
            props
        })

        // Check if the carousel items are rendered correctly
        const carouselItems = wrapper.findAll('.carousel-item')
        expect(carouselItems.length).toBe(3)
        carouselItems.forEach((item, index) => {
            expect(item.find('img').attributes('src')).toBe(props.urls[index])
        })

        // Check if the carousel indicators are rendered correctly
        const carouselIndicators = wrapper.findAll('.carousel-indicators button')
        expect(carouselIndicators.length).toBe(3)
        carouselIndicators.forEach((indicator, index) => {
            expect(indicator.attributes('data-bs-slide-to')).toBe(index.toString())
            expect(indicator.classes('active')).toBe(index === 0)
            expect(indicator.attributes('aria-current')).toBe(index === 0 ? 'true' : 'false')
        })
    })

    it('renders the previous and next buttons', () => {
        const props = {
            urls: ['image1.jpg']
        }

        const wrapper = mount(Carousel, {
            props
        })

        // Check if the previous and next buttons are rendered
        const prevButton = wrapper.find('.carousel-control-prev')
        const nextButton = wrapper.find('.carousel-control-next')
        expect(prevButton.exists()).toBe(true)
        expect(nextButton.exists()).toBe(true)
    })
})
