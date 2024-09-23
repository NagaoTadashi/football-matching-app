// middleware/auth.ts
export default defineNuxtRouteMiddleware(async (to, from) => {
    const user = await getCurrentUser();

    // redirect the user to the login page
    if (!user && to.path !== '/login') {
        return navigateTo({ path: '/login' });
    }
});
