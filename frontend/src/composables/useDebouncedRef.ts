import { ref, customRef } from 'vue'
import { debounce } from 'lodash'

function useDebouncedRef<Type>(initialValue: Type, delay: number) {
    const state = ref(initialValue)
    const debouncedRef = customRef((track, trigger) => ({
        get() {
            track()
            return state.value
        },
        set: debounce((value: any) => {
            state.value = value
            trigger()
        }, delay),
    }))
    return debouncedRef
}

export default useDebouncedRef
