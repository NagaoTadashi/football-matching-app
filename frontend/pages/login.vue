<script setup>
import { onMounted } from 'vue';

import firebase from 'firebase/compat/app';

const { $ui } = useNuxtApp();

onMounted(() => {
    $ui.start('#firebaseui-auth-container', {
        signInFlow: 'popup',
        signInSuccessUrl: '/',
        signInOptions: [firebase.auth.GoogleAuthProvider.PROVIDER_ID],
    });
});

definePageMeta({
    layout: 'login',
});
</script>

<template>
    <div id="firebaseui-auth-container"></div>
</template>
