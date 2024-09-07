// import this after install `@mdi/font` package
import '@mdi/font/css/materialdesignicons.css';
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import { VDateInput } from 'vuetify/labs/VDateInput';
import { VNumberInput } from 'vuetify/labs/VNumberInput';
import { VTimePicker } from 'vuetify/labs/VTimePicker';

export default defineNuxtPlugin((app) => {
    const vuetify = createVuetify({
        // ... your configuration
        components: {
            VDateInput,
            VNumberInput,
            VTimePicker,
        },
    });
    app.vueApp.use(vuetify);
});
