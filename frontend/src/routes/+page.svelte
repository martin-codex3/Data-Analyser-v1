<script lang="ts"></script>

<section>
  <div class="main__wrapper min-h-screen">
    <div class="grid grid-cols-12 gap-5">
      <div
        class="col-span-5 py-10 px-8 h-[calc(100vh-1rem)] overflow-auto scrollbar-thin space-y-10"
      >
        <div>
          <h1 class="text-6xl font-bold first-letter:uppercase">
            lets's get started
          </h1>
          <p class="text-gray-500 text-xl first-letter:capitalize">
            login to see what's happening
          </p>
        </div>

        <!-- for the form here  -->
        <div>
          <form action="">
            <div class="main__form__wrapper space-y-5">
              <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div class="">
                  <label for="FirstName">First name</label>
                  <input
                    type="text"
                    name="first_name"
                    id="FirstName"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                </div>

                <div class="">
                  <label for="Lastname">Last name</label>
                  <input
                    type="text"
                    name="last_name"
                    id="Lastname"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div class="">
                  <label for="Email">Email</label>
                  <input
                    type="email"
                    name="email"
                    id="Email"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                </div>

                <div class="">
                  <label for="Address">Address</label>
                  <input
                    type="text"
                    name="address"
                    id="Address"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div class="">
                  <label for="PhoneNumber">Phone number</label>
                  <input
                    type="text"
                    name="first_name"
                    id="PhoneNumber"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                </div>

                <div class="">
                  <label for="Nationality">Nationality</label>
                  <select
                    name="nationality"
                    id="Nationality"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  ></select>
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                <div class="">
                  <label for="BusinessName">Business name</label>
                  <input
                    type="text"
                    name="business_name"
                    id="BusinessName"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                </div>

                <div class="">
                  <label for="BusinessType">Business type</label>
                  <input
                    type="text"
                    name="business_type"
                    id="BusinessType"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                </div>
              </div>

              <div class="grid grid-cols-1 lg:grid-cols-1 gap-5">
                <div class="">
                  <label for="Password">Password</label>
                  <input
                    type="password"
                    name="password"
                    id="Password"
                    class="w-full py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-blue focus:ring-primary-main-blue"
                  />
                </div>
              </div>

              <div>
                <button
                  aria-label="save-button"
                  title="Create Account"
                  class="flex items-center justify-center bg-primary-main-blue first-letter:capitalize rounded-full py-3 w-54 text-blue-100"
                >
                  <span class="capitalize">create account</span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="col-span-7"></div>
    </div>
  </div>
</section>
