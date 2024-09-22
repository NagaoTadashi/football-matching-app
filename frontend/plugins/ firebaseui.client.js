import { getAuth } from 'firebase/auth';

import * as firebaseui from 'firebaseui';
import 'firebaseui/dist/firebaseui.css';

export default defineNuxtPlugin((nuxtApp) => {
    const ui = new firebaseui.auth.AuthUI(getAuth(nuxtApp.$firebaseApp));
    return {
        provide: {
            ui,
        },
    };
});
